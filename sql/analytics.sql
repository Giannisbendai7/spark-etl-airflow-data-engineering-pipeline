SELECT Car_Make,
       SUM(Sale_Price) AS total_sales
FROM car_sales
GROUP BY Car_Make
ORDER BY total_sales DESC;
