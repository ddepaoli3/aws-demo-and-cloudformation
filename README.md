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
    * networking: vpn and from onprem import services
* Global infrastructure
    * view global infrastructure with [infrastructure.aws](http://infrastructure.aws/)

## Module 2
* Autoscaling demo
* Load Balancer demo
    * balancing
    * https certificate
    * target group with different path/domain
* Autoscaling con CPU overload
* Lambda
    * creation
    * event put object S3
* S3
    * Bucket creation
    * Uploading files
    * Advanced configuration
    * Web hosting mode on S3
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
* KMS
* Secret Manager

# Cloudformation

## How to run
`aws cloudformation create-stack --stack-name discoveryday-vpc --template-body file://vpc.yml --region eu-north-1  --parameters file://vpc-parameters.json`