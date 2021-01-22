
create table real_time_stocks(
	real_time_stock_id INT NOT NULL AUTO_INCREMENT,
	update_message_type VARCHAR(100) ,
	update_time TIMESTAMP,
	Nanoseconds INT,
	Ticker VARCHAR(100),
	Bid_Size INT,
	Bid_Price INT,
	Mid_Price INT,
	Ask_Price INT,
	Ask_Size INT,
	Last_Price float,
	Last_Size INT,
	Halted INT,
	After_Hours INT,
	ISO INT,
	Oddlot INT,
	NMS_Rule INT,
	primary key (real_time_stock_id)
)