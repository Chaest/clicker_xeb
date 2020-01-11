cp /usr/share/jenkins/ref/jenkins.yml /usr/share/jenkins/ref/jenkins_old.yml
echo > /usr/share/jenkins/ref/jenkins.yml
pip3 install virtualenv
virtualenv {{ jenkins_venv_dir }}
. {{ jenkins_venv_dir }}/python/bin/activate > /dev/null 2>&1 ; pip3 install -r {{ jenkins_ref_dir }}/requirements.txt
