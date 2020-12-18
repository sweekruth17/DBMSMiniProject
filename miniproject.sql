INSERT INTO SUPPLIER VALUES (1,'Supplier1','Enterprise1','080-34567890','1234567890','supplier1@gmail.com','Bangalore');
INSERT INTO SUPPLIER VALUES (2,'Supplier2','Enterprise2','080-34567345','1234123890','supplier2@gmail.com','Mangalore');
INSERT INTO SUPPLIER VALUES (3,'Supplier3','Enterprise3','080-34567234','1534567890','supplier3@gmail.com','Mysore');


INSERT INTO PRODUCT VALUES (1, 'Teddy Bear', 100.50,200.50,1,2);
INSERT INTO PRODUCT VALUES (2, 'Toy Gun', 500.50,700.50,1,1);
INSERT INTO PRODUCT VALUES (3, 'Notebook', 50.50,70.50,2,3);
INSERT INTO PRODUCT VALUES (4, 'Notebook', 40.50,70.50,3,3);


INSERT INTO CATEGORY VALUES (1, 'Boys');
INSERT INTO CATEGORY VALUES (2, 'Girls');
INSERT INTO CATEGORY VALUES (3, 'Stationery');


INSERT INTO SELL VALUES (4,'2020-12-17',4,3);
INSERT INTO SELL VALUES (2,'2020-12-17',5,4);
INSERT INTO SELL VALUES (3,'2020-12-17',6,1);


INSERT INTO STOCK VALUES (1,20,1);
INSERT INTO STOCK VALUES (2,50,3);
INSERT INTO STOCK VALUES (3,40,4);

INSERT INTO mini_project.order VALUES (1,'2020-12-12','100', 3, 2);
INSERT INTO mini_project.order VALUES (2,'2020-12-13','50', 2, 1);
INSERT INTO mini_project.order VALUES (3,'2020-12-14','10', 4, 3);


SELECT mini_project.order.idorder, product.Product_Name, mini_project.order.Date_Ordered
FROM mini_project.order
INNER JOIN product ON mini_project.order.idProduct = product.idProduct;
