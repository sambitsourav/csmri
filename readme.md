csmri project to repository

directory structure 
csmri
---etl(implementing pipeline for real time data feed)
    ---app
    ---environment.yaml
    ---requirements.txt
    ---table_schema.sql
---trial-scripts


to create csmri environment
cd etl
conda env create -f environment.yml
conda activate csmri


to start pipeline 
-----------------
python main.py


RDS
--------
MY-SQL
for RDS details look at AWS console

####to copy files use filezilla

####ssh to awazon ec2####
ssh -i <pem file> ubuntu@<ipv4 DNS>


#### to run script in nohup
nohup python main.py &

### to see logs
cat nohup.out

#### to stop script
kill -9 `cat save.txt`