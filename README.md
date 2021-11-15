## The program update json with fast api

Retrieves json in browser on 127.0.0.1:8000

## To run the project

uvicorn main:app --reload  

### Requirements 

- Python virtual environment
- fastapi
- uvicorn

Or 
- pip install -r requirements.txt


## Json structure

![json Script](https://user-images.githubusercontent.com/72239384/141721871-ea5647ef-3d1a-4741-b8f2-dc8778af316d.PNG)

 {
  "valutaKurser": [
    {
      "fromCurrency": "DKK",
      "toCurrency": "EUR",
      "rate": 13.4480903711673
    },
    {
      "fromCurrency": "DKK",
      "toCurrency": "USD",
      "rate": 15.8997678633892
    }..
  ],
  "updatedAt": "2021-07-05T13:29:47.162734+00:00"
}

