# CloudFormation Visualizing Cross Stack References
---
### Introduction
Some time ago AWS released a feature for CloudFormation called cross stack references. (https://aws.amazon.com/blogs/aws/aws-cloudformation-update-yaml-cross-stack-references-simplified-substitution/) Cross stack references are very useful when you have parameters or resources that you need to reference in other stacks. This is extremely helpful because you can make your CloudFormation stacks much more modular and easier to maintain. For example, typically when creating infrastructure you would need to create VPC, subnet, route table, NACL, load balancer, EC2 instance, and database resources all in one CloudFormation stack. With cross stack references you can create separate stacks for network resources, application resources, databases, etc. The cross stack references can also be very useful when integrating with an existing environment or CloudFormation template as you can retrieve VPC ID's, Subnet ID's, etc. and use them within a new stack. Cross stack references save a lot of manual work, where previously you would need to look up all the ID's needed and add them to parameters, or create Lambda functions to retrieve the ID's.

![Image](http://www.n2ws.com/images/cloudformation.jpg)

Cross stack references are created by adding an “Export” declaration to a normal CloudFormation stack output and using a new built in function to access them. That new function, Fn::ImportValue, does have a few restrictions that are important to note if you are setting out on creating your first cross-stack reference with it. Namely, the export names must be unique within an account and region, and the function will not allow you to create references across regions. In addition, AWS will not allow you to delete a stack that is being referenced by another stack and your outputs cannot be changed or removed while they are being referenced by a stack.

### The Problem
There is one problem with cross stack references. When your infrastructure is fairly complex with multiple stacks and many references within those stacks, it can be very difficult to see and understand all the connections and references. Then when it comes time to make changes to a resource or reference it can be hard to see where those changes will have an impact.

### The Solution
To solve the problems with complex cross stack references, I fell back to my tried and trusted friends data, analysis, and visualization. In this case not much analysis was needed. All that's needed, in this case, is some way to get data about all the cross stack references, and then some way to visualize them.

### Getting the Data
To get the necessary data I used the AWS Python SDK Boto3 (https://aws.amazon.com/sdk-for-python/). I first hit the AWS account and retrieve all the CloudFormation exports and the name of the template from which they are being exported. I then iterate over all those exports and retrieve all the places where they are being imported and the name of that template. I then write the output to a json file that will be used for the visualization. Here is a link to my code: (https://github.com/ACHepcat/cf-cross-stack-mapping/blob/master/get_data_v2.py)

### D3 and the Sankey Diagram
The next step was to somehow show all the connections between all the stacks and all the exports and imports. To accomplish this I chose to use a Sankey Diagram (https://en.wikipedia.org/wiki/Sankey_diagram). I chose the Sankey Diagram instead of the usual Network Diagram mainly because I wanted to see the flow of the references between the stacks versus just the connections. Sankey Diagrams are not in your typical visualization tools. So, to show and share the visualization I chose to use the D3 javascript library (https://d3js.org/). D3 is easy to use and it creates a nice visualization that is easy to view and share with any modern web browser. The other nice feature of the D3 Sankey Diagram is that it is interactive, and you can grab the nodes that represent the stacks and move them around as needed. I also experimented with a Flare Chart for a different type of view, however, the Flare Chart lacked a way to show the interconnections that I wanted to be able to see. The code for the D3 visuals can be found here (https://github.com/ACHepcat/cf-cross-stack-mapping). Example visualizations can be seen here (https://achepcat.github.io/)

### Summary and Conclusions.
In the end a customer can see the complete relationships between all the stacks in their environment. So far the most useful feature has been to see when there are exports that are not being used and removing them to make the cross stack references more efficient and easier to maintain. The other thing this may be useful for is to see an overall picture of your AWS infrastructure and how things are related within it.

**Some future considerations:**
Better color coding of the nodes. For instance, one color to denote stacks and another color to denote exports.
