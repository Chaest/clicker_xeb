output "jenkins_public_dns" {
  value = "${aws_instance.jenkins.public_dns}"
}
output "jenkins_public_ip" {
  value = "${aws_instance.jenkins.public_ip}"
}
{% for env_name in environments %}
output "{{ env_name }}_public_dns" {
  value = "${aws_instance.{{ env_name }}.public_dns}"
}
output "{{ env_name }}_public_ip" {
  value = "${aws_instance.{{ env_name }}.public_ip}"
}
{% endfor %}
