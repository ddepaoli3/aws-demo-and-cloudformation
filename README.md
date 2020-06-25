README
======
This repository is used as guide and reference for AWS discovery day (June 2020).


# Demo
List of possible demo to show in different modules

## Module 1
* Demo console:
    * AWS console
    * EC2 scalable instances
    * on demand prices
    * EC2 elasticity
    * networking
    * storage gateway
* Global infrastructure
    * view global infrastructure with [infrastructure.aws](http://infrastructure.aws/)

## Module 2
* Autoscaling demo
    * CPU overload
* System manager run command
* Load Balancer demo
    * balancing
    * https certificate
    * target group with different path/domain
* S3
    * Bucket creation
    * Uploading files
    * Advanced configuration
    * Web hosting mode on S3
* Lambda
    * creation
    * event put object S3
* EBS
    * EBS creation
    * EC2 attacchment
    * use EBS on EC2
    * Snapshot
* EFS
    * creation
    * EC2 mount
* RDS
    * creation
    * connection to RDS
* Dynamodb
    * tables creation
    * inserting data into dynamodb
* Networking
    * VPC
    * Route53
    * Cloudfront

## Module 3
* IAM

# Cloudformation

## How to run
`aws cloudformation create-stack --stack-name discoveryday-vpc --template-body file://vpc.yml --region eu-north-1  --parameters file://vpc-parameters.json`

`aws cloudformation create-stack --stack-name discoveryday-autoscaling --template-body file://autoscaling.yml --region eu-north-1  --parameters file://autoscaling-parameters.json --capabilities CAPABILITY_IAM`

`aws cloudformation create-stack --stack-name discoveryday-efs --template-body file://efs.yml --region eu-north-1  --parameters file://efs-parameters.json`

# Note

## Bucket policy web hosting
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": [
                "s3:GetObject"
            ],
            "Resource": [
                "arn:aws:s3:::example.com/*"
            ]
        }
    ]
}
```

## Command to run in ec2 with System Manager
```
sudo apt update
sudo apt install stress apache2 --yes
```