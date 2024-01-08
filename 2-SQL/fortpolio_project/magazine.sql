CREATE TABLE magazines(
	id SERIAL PRIMARY KEY,
	category TEXT NOT NULL,
	title TEXT NOT NULL UNIQUE,
	start_date DATE NOT NULL DEFAULT now()
);

CREATE TABLE customers(
	customer_id SERIAL PRIMARY KEY,
	first_name TEXT NOT NULL,
	last_name TEXT NOT NULL,
	subscribe_date DATE NOT NULL DEFAULT now(),
	country TEXT
);

CREATE TABLE sponsers(
	id SERIAL PRIMARY KEY,
	first_name TEXT,
	last_name TEXT,
	company_name TEXT NOT NULL,
	url CHAR UNIQUE,
	email CHAR NOT NULL UNIQUE
);

CREATE TABLE articles(
	id SERIAL PRIMARY KEY,
	magazine_id INT NOT NULL,
	category TEXT NOT NULL,
	title TEXT NOT NULL,
    author_name TEXT NOT NULL DEFAULT 'Partnership',
	published_date TIMESTAMP DEFAULT now()
);

CREATE TABLE authors (
	id SERIAL PRIMARY KEY,
	first_name TEXT NOT NULL,
	last_name TEXT NOT NULL,
	email TEXT NOT NULL UNIQUE,
	supervisor_id INT
);

CREATE TABLE supervisors(
	id SERIAL PRIMARY KEY,
	first_name TEXT NOT NULL,
	last_name TEXT NOT NULL,
	email CHAR NOT NULL UNIQUE
);


-- for many-to-many relationships: magazines & customers
CREATE TABLE subscribe_magazines(
	magazine_id INT,
	user_id INT,
	start_date DATE NOT NULL DEFAULT now(),
	PRIMARY KEY (magazine_id, user_id)
);

-- for many-to-many relationships: magazines & sponsers
CREATE TABLE sponsered_by (
	magazine_id INT,
	sponser_id INT,
	cost FLOAT(2) NOT NULL DEFAULT 0.00,
	end_date DATE,
	start_date DATE NOT NULL DEFAULT now(),
	PRIMARY KEY (magazine_id, sponser_id)
);



-- alter table: set foriegn key
-- magazines & subscribe_magazines
ALTER TABLE subscribe_magazines
ADD CONSTRAINT fk_sm_magazines
FOREIGN KEY (magazine_id)
REFERENCES magazines;
-- subscribe_magazines & customers
ALTER TABLE subscribe_magazines
ADD CONSTRAINT fk_sm_customers
FOREIGN KEY (user_id)
REFERENCES customers;

-- magazines & sponsered_by
ALTER TABLE sponsered_by
ADD CONSTRAINT fk_sponsered_magazines
FOREIGN KEY (magazine_id)
REFERENCES magazines;
-- sponsered_by & sponsers
ALTER TABLE sponsered_by
ADD CONSTRAINT fk_sponsered_sponsers
FOREIGN KEY (sponser_id)
REFERENCES sponsers;

-- magazines & articles
ALTER TABLE articles
ADD CONSTRAINT fk_articles_magazines
FOREIGN KEY (magazine_id)
REFERENCES magazines;

-- authors & articles
ALTER TABLE articles
ADD CONSTRAINT fk_articles_authors
FOREIGN KEY (author_id)
REFERENCES authors(id);
-- authors & supervisors
ALTER TABLE authors
ADD CONSTRAINT fk_authors_supervisors
FOREIGN KEY (supervisor_id)
REFERENCES supervisors;


-- insert data
INSERT INTO magazines (title,category,start_date)
VALUES ('The Intellic Homes','Home','2020-02-17'),
('Daily Spots','General News','1999-12-09'),
('Cookings','Cook','2008-03-29'),
('Art Tech','Art','2017-04-20'),
('Health Tech','Health','2022-08-03'),
('Environmental Now','Environment','2015-12-12');

INSERT INTO customers (first_name,last_name,subscribe_date,country)
VALUES ('Frank','Ace','2004-03-01',null),
('Scott','Adams','1998-02-17','GBR'),
('Estelle','Lee','2018-08-23','KOR'),
('Jane','Mitch','1973-12-04','BEL'),
('Tariq','W.C','1997-01-02','CAN'),
('Bach','Richard','2003-03-08','COL'),
('Mikhail','Kim','2017-03-08','KOR'),
('Cannon','James P','2000-03-08','CAN'),
('Mick','Foley','2000-03-08','GBR'),
('Cannon','James P','2001-09-30',null),
('Cannon','James P','2023-01-05','DMA'),
('Fiske','Irving','2022-07-26',null),
('Fuller','Margaret','2010-12-25',null),
('Gandhi','Maha','2006-06-25','IND'),
('Goya','Francisco','1997-05-15','ITA'),
('Holt','Anatol','2002-08-31',null),
('Adolf','Joe','2024-01-04',null),
('Nahye','Yoon','2003-03-08','KOR');

INSERT INTO sponsers (first_name,last_name,company_name,url,email)
VALUES ('Joe','Brazil','Sports Distict',null,'joebrazil@gmail.com'),
('Mark','Pilhy','Notes World','https://notesworld.com','markpilhy@gmail.com'),
('Elysom','Butcher','Real Cook','http://realcook.co.uk','elysombutcher@gmail.com'),
('Kelty','Mayo','Greener',null,'keltymayo@yahoo.com'),
('Steve','Amadon','Daily News','http://dailynews.com','steveamadon@gmail.com'),
('Bache','Mozad','Paints','http://paintsmozad.com','bachemozad@yahoo.com'),
('Adam','Raily','Home Direct',null,'adamraily@homedirect.com'),
('Holiet','Mitch','Earthfull','https://earthfull.com','holietmitch@earthfull.com');


INSERT INTO articles (title,magazine_id,category,published_date)
VALUES ('This Ultrasound Bra Could Detect Cancer Sooner',5,'Wearable','2024-01-03'),
('The Plan to Put Pig Genes in Soy Beans for Tastier Fake Meat',3,'Genetics','2024-01-02'),
('The 18 Best EVs Comming in 2024',2,'Cars','2024-01-01'),
('Your Eco-Friendly Lifestyle Is a Big Lie',6,'Environment','2023-12-29'),
('Spying on Beavers From Space Could Help Save California',6,'Animals','2023-12-28'),
('Google Fixes Nearly 100 Android Security Issues',2,'Security','2023-12-31'),
('Undersea-Aged Champagne Is Starting to Surface',3,'Gear','2023-12-23'),
('Lamborghini''s Revuelto Is the Outstanding Hybrid of 2023',2,'Cars','2023-12-19'),
('Tesla Is Recalling Nearly All Vehicles Sold in US to Fix an Autopilot Fault',2,'Cars','2023-12-13'),
('Panasonic''s New Powder-Powered Batteries Will Supercharge EVs',2,'Cars','2023-12-12'),
('Former NBA Star Rick Fox Is Making a Play for Carbon-Neutral Concrete',6,'Planet Pioneers','2024-01-03'),
('A Demographic Time Bomb Is About to Hit the Beef Industry',3,'Environment','2023-12-21'),
('Scammers Are Tricking Anti-Vaxxers Into Buying Bogus Medical Documents',2,'Security','2023-12-18'),
('Energy Drinks Are Out of Control',5,'Drinks','2023-12-15'),
('Stop Planting Trees, Says Guy Who Inspired World to Plant a Trillion Trees',6,'Environment','2023-12-13'),
('EV Batteries Have a Dirty Secret. This Company Has a Plan to Clean Them Up',6,'Planet Pioneers','2023-11-08'),
('How to Set Up a Home Office That Can Survive a Power Outage',1,'Gear','2023-07-09'),
('Immersive Multi-Room Audio Comes Home',1,'Music','2022-12-01'),
('How LG is Quietly Building Out its Eco-Friendly, Energy Efficient Smart Home',1,'Appliances','2023-01-27'),
('In the Future, Patients Won''t Go to the Hospital-It Will Come to Them',5,'Health','2023-06-26'),
('Augmented Reality Art Takes Over the Roofs of a British City',4,'Gear','2023-04-24');

author:
Grace Browne
Matt Reynolds
Jeremy White
Matt Reynolds
Ben Goldfarb
Kate O'Flaherty
Alice Lascelles
Jeremy White
Jeremy White
Carlton Reid
Peter Guest
Matt Reynolds
Matt Burgess
Tom Ward
Alec Luhn
Rob Reddick
David Nield
Partnership
Partnership
Tara Donnelly
Elissaveta M. Brandon

INSERT INTO authors (first_name,last_name,email)
VALUES ('Partnership',null,null),
('Grace','Browne','gracebrowne@gmail.com'),
('Matt','Reynolds','mattreynolds@gmail.com'),
('Jeremy','White','jeremywhite@gmail.com'),
('Ben','Goldfarb','bengoldfarb@gmail.com'),
('Kate','O''Flaherty','kateoflaherty@gmail.com'),
('Alice','Lascelles','alicelascelles@gmail.com'),
('Carlton','Reid','carltonreid@gmail.com'),
('Peter','Guest','peterguest@gmail.com'),
('Matt','Burgess','mattburgess@gmail.com'),
('Tom','Ward','tomward@gmail.com'),
('Alec','Luhn','alecluhn@gmail.com'),
('Rob','Reddick','robreddick@gmail.com'),
('David','Nield','davidnield@gmail.com'),
('Tara','Donnelly','taradonnelly@gmail.com'),
('Elissaveta','M. Brandon','elissavetam_brandon@gmail.com');

INSERT INTO supervisors (first_name,last_name,email)
VALUES ('Matt','Reynolds','mattreynolds@gmail.com'),
('Jeremy','White','jeremywhite@gmail.com');