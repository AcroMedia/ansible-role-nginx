# Testing with Molecule

## Quick start with default test scenario
```bash
pip install molecule
molecule test
```

## Testing all distro variations with Tox

See https://tox.readthedocs.io/en/latest/

See [tox.ini](./tox.ini) for the distro variants being tested against.

```bash
pip install tox
tox
```

## Advanced

### Setup Local Virtual Environment

- to run a single test
```bash
python3 -m venv venv
source venv/bin/activate
pip3 install 'molecule[docker]'
pip3 install -r requirements.txt
MOLECULE_DISTRO=centos7 molecule test
```

- note that you can substitute MOLECULE_DISTRO=version for the following:

__MOLECULE_DISTRO List__

    centos7
    centos8

    debian8
    debian9
    debian10

    ubuntu1604
    ubuntu1804

- look here for more images: https://hub.docker.com/r/geerlingguy/

### Development

- if you are creating a new molecule test suite inside an existing role then execute this ...
```bash
molecule init scenario -r ansible-role-nginx
```
- you can change one line and enter a different molecule command to keep the container alive
    - from the ```MOLECULE_DISTRO``` list above, substitute your desired version for development below

```yaml
# /molecule/default/molecule.yml
  image: "geerlingguy/docker-${MOLECULE_DISTRO:-debian9}-ansible:latest"
```

- run this command so that the container is not dead
```bash
molecule test --destroy=never
```

- ssh into the container after the test
```bash
molecule login
```

- run the test suite located in ```molecule/test/test_default.py```
```bash
molecule verify
```
