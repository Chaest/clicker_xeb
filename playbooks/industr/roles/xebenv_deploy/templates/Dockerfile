FROM tomcat:jdk8

ENV REDIS_HOST {{ env_type }}_redis_1

RUN apt update && apt install -y openssh-server sudo python
RUN mkdir /var/run/sshd

RUN useradd -ms /bin/bash {{ jenkins_to_back_user }}
RUN echo "{{ jenkins_to_back_user }}:{{ jenkins_to_back_password }}" | chpasswd
RUN adduser {{ jenkins_to_back_user }} sudo
RUN echo "{{ jenkins_to_back_user }} ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd


RUN mkdir -p {{ jenkins_to_back_ssh_dir }}
COPY {{ ssh_key_name }}.pub {{ jenkins_to_back_ssh_dir }}/authorized_keys
RUN chmod 700 {{ jenkins_to_back_ssh_dir }}
RUN chown {{ jenkins_to_back_user }} {{ jenkins_to_back_ssh_dir }}
RUN chmod 600 {{ jenkins_to_back_ssh_dir }}/authorized_keys
RUN chown {{ jenkins_to_back_user }} {{ jenkins_to_back_ssh_dir }}/authorized_keys

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

ADD wrapper.sh /

EXPOSE 22
RUN chmod +x /wrapper.sh
CMD /wrapper.sh
