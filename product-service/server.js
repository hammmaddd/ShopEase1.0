const express = require('express');
const app = express();
app.use(express.json());

app.get('/products', (req, res) => {
    // Placeholder for fetching products
    res.json([{ id: 1, name: "Product A" }]);
});

app.listen(process.env.PORT || 3000, () => {
    console.log(`Product service running on port ${process.env.PORT || 3000}`);
});