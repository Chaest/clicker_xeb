FROM jenkins/jenkins:latest

USER root

ENV JAVA_OPTS="-Djenkins.install.runSetupWizard=false -Djenkins.CLI.disabled=true ${JAVA_OPTS:-} -Dorg.apache.commons.jelly.tags.fmt.timeZone=Europe/Paris -Dhudson.security.csrf.DefaultCrumbIssuer.EXCLUDE_SESSION_ID=true"
ENV VENV_HOME="{{ jenkins_venv_dir }}"

{% for file in jenkins_ref_files %}
COPY {{ file }} {{ jenkins_ref_dir }}/{{ file }}
{% endfor %}

RUN mkdir -p {{ jenkins_ssh_dir }}
COPY {{ ssh_key_name }} {{ jenkins_ssh_dir }}/{{ ssh_key_name }}
COPY {{ ssh_key_name }}.pub {{ jenkins_ssh_dir }}/{{ ssh_key_name }}.pub
RUN chmod 700 {{ jenkins_ssh_dir }}
RUN chmod 600 {{ jenkins_ssh_dir }}/{{ ssh_key_name }}
RUN chmod 640 {{ jenkins_ssh_dir }}/{{ ssh_key_name }}.pub

# Preparing environment
RUN apt-get update
RUN apt-get install -y python-pip sudo libaio1 unzip sshpass rsync maven
RUN pip install virtualenv
RUN virtualenv {{ jenkins_venv_dir }}
RUN {{ jenkins_venv_dir }}/bin/pip --no-cache-dir install -r {{ jenkins_ref_dir }}/requirements.txt 
RUN sh {{ jenkins_ref_dir }}/selenium_prepare.sh
RUN env && /usr/local/bin/install-plugins.sh < {{ jenkins_ref_dir }}/plugins.txt
