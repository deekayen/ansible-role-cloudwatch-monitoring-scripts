AWS CloudWatch monitoring scripts
=========

[![Build Status](https://travis-ci.org/deekayen/ansible-role-cloudwatch-agent-scripts.svg?branch=master)](https://travis-ci.org/deekayen/ansible-role-cloudwatch-agent-scripts)

An Ansible role to install AWS Cloudwatch Logs agent and monitoring scripts on Enterprise Linux.

Please see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/QuickStartEC2Instance.html

We also install the monitoring script for linux to monitor memory, cpu, swap, etc.
You need to have a role attach to the instance (or credentials) in order to be able to write to cloudwatch.

See: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/mon-scripts.html


Requirements
------------



Role Variables
--------------

A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.

Dependencies
------------

```
- src: git+https://github.com/riponbanik/ansible-role-aws-cloudwatch-agent.git
  name: riponbanik.aws-cloudwatch-agent
  version: 80203e57822b3c1424460a9d222f47f668e114e7
```

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: all
      roles:
        - deekayen.cloudwatch_monitoring_scripts

License
-------

MIT




**Monitoring scripts for linux**


## Usage

Include the folder in your roles directory.

If you want to run this playbook locally you can do the following.

Clone the repository

```shell
git clone https://github.com/bitintheskud/ansible-role-cloudwatch-logs-agent.git
```
Create a local ansible playbook with the role included.

```Shell
cat > playbook.yml
---
- name: Test cloudwatch role
  hosts: 127.0.0.1
  become: yes
  roles:
    - { role: '<YOUR PATH>/ansible-role-cloudwatch-logs-agent' }
```

Run ansible-playbook

```shell
ansible-playbook  -i "localhost," -c local playbook.yml
```

You need to attach a role to your instance to send message to AWS Cloudwatch.

see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/QuickStartEC2Instance.html
