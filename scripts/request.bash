# Create a new product_code
curl -X POST http://0.0.0.0:3000/create_tag -H 'Content-Type: application/json' -d '{"product_code":"teste"}' -i

# Create validation
curl -X POST http://0.0.0.0:3000/create_tag -H 'Content-Type: application/json' -d '{"product_cod":"teste"}' -i
