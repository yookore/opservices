This file contains bosh deployment configuration for docker. As part of docker
container services contained in this release are:
- postgresql
- mysql
- redis
- couchdb
- rethinkdb
- memcached

Do deploy to a running CF installation:
- Modify deployment.yml accordingly
- bosh target <BOSH_HOST>
- git clone https://github.com/cf-platform-eng/docker-boshrelease.git
- cd docker-boshrelease
- bosh upload release releases/docker/docker-13.yml
- bosh deployment path/to/deployment.yml
- bosh -n deploy
