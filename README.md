
# Ouo.io bypasser

A script to automatically bypass any link thats shorten with ouo.io




## API Reference

#### Get all items

```http
  GET /bypass?url=https://ouo.io/abc
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `url` | `string` | **Required**. The ouo.io url |


## Demo

https://ouo-bypasser.onrender.com


## Run Locally

Clone the project

```bash
  git clone https://github.com/fpesce27/ouo-bypasser
```

Go to the project directory

```bash
  cd ouo-bypasser
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  python app.py
```

