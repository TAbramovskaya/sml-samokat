# Samokat Sales Analysis

## Data Description

### `products` table

| Column       | Description         |
| ------------ | ------------------- |
| `product_id` | Product ID          |
| `level1`     | Product category    |
| `level2`     | Product subcategory |
| `name`       | Product name        |

### `orders` table

| Column          | Description                          |
| --------------- | ------------------------------------ |
| `order_id`      | Order/receipt ID                     |
| `accepted_at`   | Order/receipt date and time          |
| `product_id`    | Product ID                           |
| `quantity`      | Quantity of the product in the order |
| `regular_price` | Regular price                        |
| `price`         | Current selling price                |
| `cost_price`    | Purchase cost                        |

[Source data](https://disk.yandex.ru/d/EkSfw6q9qLKmNA)

## Tasks

### Best-Selling Product Category

Which product category has the highest number of units sold?

1. Support the answer with a table showing the total number of units sold for each product category.
2. Build a bar chart based on this table.
3. Make sure that all chart labels are clear and readable. The chart should be immediately understandable to an external observer.

### Sales Distribution by Subcategory

Analyze the distribution of the number of units sold within each product category (`level1`) across its subcategories (`level2`).

Present the results in a summary table.

### Average Order Value on a Specific Date

What was the average order value on January 13, 2022?

### Promotional Sales Share by Category

When a product is sold as part of a promotion, its regular price differs from its actual selling price.

1. Calculate the share of promotional sales, in units, among all sales in the `Cheeses` category.
2. Build a pie chart to illustrate the result. The chart should clearly show the groups, their respective shares, and understandable labels.

### Margin by Category

Calculate the margin for all `level1` categories:

1. Margin in RUB.
2. Margin as a percentage.

Visualize the results using two horizontal bar charts. All labels should be clear and readable.

### ABC Analysis

1. Perform an ABC analysis of sales by quantity.
2. Perform an ABC analysis of sales by revenue.
3. Create a new column containing the combined ABC group based on the results of both analyses. For example: `A C`.

**Important:** The ABC analysis should be performed **at the subcategory level**, rather than at the individual product level. The available data covers a relatively short period, which is insufficient for a meaningful product-level analysis. In addition, the large number of individual products could distort the results. An ABC analysis at the subcategory level should provide a more meaningful and interpretable picture.

**Additional note:** For all tasks except the average order value calculation, products listed in `orders` but missing from `products` may be excluded from the analysis.
