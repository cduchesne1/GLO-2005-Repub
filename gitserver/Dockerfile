# Inspired from https://linuxhint.com/setup_git_http_server_docker/

FROM ubuntu:18.04

RUN apt update 2>/dev/null
RUN apt install -y git apache2 apache2-utils 2>/dev/null
RUN a2enmod env cgi alias rewrite
RUN mkdir /var/www/git
RUN git config --global --add safe.directory /var/www/git
RUN chown -Rfv www-data:www-data /var/www/git

COPY ./git-shell/git.conf /etc/apache2/sites-available/git.conf
COPY ./git-shell/git-create-repo.sh /usr/bin/mkrepo
COPY ./git-shell/git-delete-repo.sh /usr/bin/rmrepo
COPY ./git-shell/git-list-repos.sh /usr/bin/lsrepos
COPY ./git-shell/git-list-files.sh /usr/bin/lsfiles
COPY ./git-shell/git-list-branches.sh /usr/bin/lsbranches
COPY ./git-shell/git-show-file-content.sh /usr/bin/showcontent
RUN chmod +x /usr/bin/mkrepo
RUN chmod +x /usr/bin/rmrepo
RUN chmod +x /usr/bin/lsrepos
RUN chmod +x /usr/bin/lsfiles
RUN chmod +x /usr/bin/lsbranches
RUN chmod +x /usr/bin/showcontent

RUN a2dissite 000-default.conf
RUN a2ensite git.conf
RUN git config --system http.receivepack true
RUN git config --system http.uploadpack true
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_LOCK_DIR /var/lock/apache2
ENV APACHE_PID_FILE /var/run/apache2.pid
CMD /usr/sbin/apache2ctl -D FOREGROUND

EXPOSE 80/tcp