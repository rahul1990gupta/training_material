Create an account in AWS. Also install the command line aws python utility. 
- S3: Put some data in a custom S3 bucket. You can do this by either with command line or directly uploading the data through UI. 
- EC2: Create an EC2 instance(t2.micro) and run a simple python http server. Make sure that you can access the web service with the machine's IP.
- EBS: Attach the EBS to EC2 instance. Write some data on the EBS mount. You should be able to access the data on the EBS volume with another EC2 instance even after the first instance dies down.
- RDS: Create a postgresql RDS instance. You should be able to connect with this RDS instance from your local machine. load the sakilla database and query it from your command line. 
- Athena: Execute a "getting started" guide to get familiar with querying the data with Athena.
- EMR: First, setup spark cluster locally and run the job locally. Get familiar with running a job on EMR 
- EKS: install and launch a kubernetes cluster locally. Launch an EKS cluster and run a simple service. 
- After a month of these experiemnt, review the Bills to see how AWS charges for different services. 


Note: 
- Make sure to delete all the resources after you are done.
