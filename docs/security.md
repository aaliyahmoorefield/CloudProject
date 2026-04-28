# Security

## Security Goals
- Protect parking and vehicle-related data  
- Prevent unauthorized access  
- Maintain system availability  
- Monitor suspicious activity  

## Risks
- Unauthorized access to parking data  
- Misconfigured cloud permissions  
- Data interception during transmission  
- Service outages or denial-of-service attacks  
- Exposure of credentials or API keys  

## Security Controls

### Cloud IAM
IAM is used to control access to cloud resources. Role-based access ensures users and services only have the permissions they need.

### Secret Manager
Secret Manager stores sensitive information such as API keys, passwords, and configuration values securely.

### Encryption
Data is protected using encryption both in transit and at rest to prevent interception and unauthorized access.

### Cloud Logging
Cloud Logging records system activity, which helps detect unusual behavior or security issues.

### Cloud Monitoring
Cloud Monitoring tracks system performance and can alert administrators of potential threats or failures.

### Least Privilege
The system follows the principle of least privilege, meaning users and services only get the minimum access required.

### Secure API Design
APIs are designed with authentication and validation to ensure only authorized users can interact with the system.

## Security Summary
This security approach protects the smart parking system by using access control, encryption, monitoring, and secure design practices. These measures help reduce risks and keep the system reliable and secure.
