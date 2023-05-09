package main

import (
	"net/http"
	"strconv"

	"github.com/labstack/echo/v4"
)

type Product struct {
	ID    int    `json:"id"`
	Name  string `json:"name"`
	Price int    `json:"price"`
}

type Payment struct {
	ID        int    `json:"id"`
	CardNo    string `json:"cardNo"`
}


type Products []Product
type Payments []Payment

var products = Products{
	{ID: 1, Name: "Product 1", Price: 100},
	{ID: 2, Name: "Product 2", Price: 200},
}

var payments = Payments{}

func main() {
	e := echo.New()

	// GET all products
	e.GET("/products", func(c echo.Context) error {
		return c.JSON(http.StatusOK, products)
	})

	// GET product by ID
	e.GET("/products/:id", func(c echo.Context) error {
		id, _ := strconv.Atoi(c.Param("id"))
		for _, p := range products {
			if p.ID == id {
				return c.JSON(http.StatusOK, p)
			}
		}
		return echo.NewHTTPError(http.StatusNotFound, "Product not found")
	})

	// POST new product
	e.POST("/products", func(c echo.Context) error {
		p := new(Product)
		if err := c.Bind(p); err != nil {
			return err
		}
		p.ID = len(products) + 1
		products = append(products, *p)
		return c.JSON(http.StatusCreated, p)
	})

	// PUT update product by ID
	e.PUT("/products/:id", func(c echo.Context) error {
		id, _ := strconv.Atoi(c.Param("id"))
		for i := range products {
			if products[i].ID == id {
				p := new(Product)
				if err := c.Bind(p); err != nil {
					return err
				}
				p.ID = id
				products[i] = *p
				return c.JSON(http.StatusOK, p)
			}
		}
		return echo.NewHTTPError(http.StatusNotFound, "Product not found")
	})

	// DELETE product by ID
	e.DELETE("/products/:id", func(c echo.Context) error {
		id, _ := strconv.Atoi(c.Param("id"))
		for i := range products {
			if products[i].ID == id {
				products = append(products[:i], products[i+1:]...)
				return c.NoContent(http.StatusNoContent)
			}
		}
		return echo.NewHTTPError(http.StatusNotFound, "Product not found")
	})


	e.POST("/payments", func(c echo.Context) error {
		p := new(Payment)
		if err := c.Bind(p); err != nil {
			return err
		}
		p.ID = len(payments) + 1
		payments = append(payments, *p)
		return c.JSON(http.StatusCreated, p)
	})

	e.Logger.Fatal(e.Start(":8080"))
}