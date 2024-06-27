const express = require('express');
const redis = require('redis');
const { promisify } = require('util');
const app = express();
const port = 1245;

const listProducts = [
  { id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
  { id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
  { id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
  { id: 4, name: 'Suitcase 1050', price: 550, stock: 5 },
];

function getItemById(id) {
  return listProducts.find((product) => product.id === id);
}

const client = redis.createClient();

const reserveStockById = (itemId, stock) => {
  client.set(`item.${itemId}`, stock, redis.print);
};

const getCurrentReservedStockById = async (itemId) => {
  const getAsync = promisify(client.get).bind(client);
  const stock = await getAsync(`item.${itemId}`);
  return stock;
};

app.get('/list_products', (req, res) => {
  const products = listProducts.map((product) => ({
    itemId: product.id,
    itemName: product.name,
    price: product.price,
    initialAvailableQuantity: product.stock,
  }));
  res.json(products);
});

app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const item = getItemById(itemId);

  if (!item) {
    return res.json({ status: 'Product not found' });
  }

  const reservedStock = await getCurrentReservedStockById(itemId);
  const currentQuantity =
    reservedStock !== null ? item.stock - reservedStock : item.stock;

  res.json({
    itemId: item.id,
    itemName: item.name,
    price: item.price,
    initialAvailableQuantity: item.stock,
    currentQuantity: parseInt(currentQuantity),
  });
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const item = getItemById(itemId);

  if (!item) {
    return res.json({ status: 'Product not found' });
  }

  const reservedStock = await getCurrentReservedStockById(itemId);
  const currentQuantity =
    reservedStock !== null ? item.stock - reservedStock : item.stock;

  if (currentQuantity <= 0) {
    return res.json({ status: 'Not enough stock available', itemId: item.id });
  }

  reserveStockById(item.id, parseInt(reservedStock) + 1);
  res.json({ status: 'Reservation confirmed', itemId: item.id });
});

app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});
