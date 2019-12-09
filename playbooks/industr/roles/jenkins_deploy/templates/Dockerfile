FROM jenkins/jenkins:latest

USER root

ENV JAVA_OPTS="-Djenkins.install.runSetupWizard=false -Djenkins.CLI.disabled=true ${JAVA_OPTS:-} -Dorg.apache.commons.jelly.tags.fmt.timeZone=Europe/Paris -Dhudson.security.csrf.DefaultCrumbIssuer.EXCLUDE_SESSION_ID=true"
ENV VENV_HOME="{{ jenkins_venv_dir }}"

{% for file in jenkins_ref_files %}
COPY {{ file }} {{ jenkins_ref_dir }}/{{ file }}
{% endfor %}

# Preparing environment
RUN apt-get update
RUN apt-get install -y python-pip sudo libaio1 unzip sshpass rsync maven
RUN pip install virtualenv
RUN sh {{ jenkins_ref_dir }}/selenium_prepare.sh
RUN env && /usr/local/bin/install-plugins.sh < {{ jenkins_ref_dir }}/plugins.txt
