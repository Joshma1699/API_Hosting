
CREATE TABLE plans (
    Category VARCHAR(100) NOT NULL, 
    Plans VARCHAR(100) NOT NULL, 
    Created_By VARCHAR(100),
    Created_Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    Last_Update_By VARCHAR(100),
    Last_Update_Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP NOT NULL
);


INSERT INTO plans (Category,Plans,Created_By,Last_Update_By)
VALUES 
('Business Internet','Business Internet 300 Mbps','admin', 'admin'),
('Business Internet','Business Internet Gigabit', 'admin', 'admin'),
('Business Internet','Business Internet 2 Gigabit', 'admin', 'admin'),
('Business TV','Rogers Xfinity Business TV Basic', 'admin', 'admin'),
('Business TV','Rogers Xfinity Business TV Premium', 'admin', 'admin'),
('Business Mobile','Advantage Mobility','admin', 'admin'),
('Business Mobile', '5G Infinite Essential','admin', 'admin'),
('Business Mobile', '5G Infinite Extra','admin', 'admin'),
('Business Mobile', '5G Infinite Premium','admin', 'admin');


UPDATE plans 
SET Plans = 'Xfinity Business TV Basic' 
WHERE Plans = 'Rogers Xfinity Business TV Basic';

UPDATE plans 
SET Plans = 'Xfinity Business TV Premium' 
WHERE Plans = 'Rogers Xfinity Business TV Premium';

INSERT INTO plans (Category,Plans,Created_By,Last_Update_By)
VALUES 
('Business Internet & TV','Business Internet 300 Mbps and Basic','admin', 'admin');

SELECT * FROM plans;