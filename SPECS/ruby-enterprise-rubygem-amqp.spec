%define ruby_dist ruby-enterprise
%define ruby_dist_dash %{ruby_dist}-
%define _prefix /opt/ruby-enterprise
%define _gem %{_prefix}/bin/gem
%define _ruby %{_prefix}/bin/ruby

# Generated from amqp-0.6.7.gem by gem2rpm -*- rpm-spec -*-
%define ruby_sitelib %(%{_ruby} -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define gemdir %(%{_ruby} -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gemname amqp
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: AMQP client implementation in Ruby/EventMachine
Name: %{?ruby_dist_dash}rubygem-%{gemname}
Version: 0.6.7
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://amqp.rubyforge.org/
Source0: %{gemname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: %{?ruby_dist_dash}rubygems
Requires: %{?ruby_dist_dash}rubygem(eventmachine) >= 0.12.4

BuildRequires: rubygems
BuildArch: noarch
Provides: %{?ruby_dist_dash}rubygem(%{gemname}) = %{version}

%description
An implementation of the AMQP protocol in Ruby/EventMachine for writing
clients to the RabbitMQ message broker


%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gemdir}
%{_gem} install --local --install-dir %{buildroot}%{gemdir} \
                --force --rdoc %{SOURCE0}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{gemdir}/gems/%{gemname}-%{version}/
%doc %{gemdir}/doc/%{gemname}-%{version}
%doc %{geminstdir}/README
%doc %{geminstdir}/doc/EXAMPLE_01_PINGPONG
%doc %{geminstdir}/doc/EXAMPLE_02_CLOCK
%doc %{geminstdir}/doc/EXAMPLE_03_STOCKS
%doc %{geminstdir}/doc/EXAMPLE_04_MULTICLOCK
%doc %{geminstdir}/doc/EXAMPLE_05_ACK
%doc %{geminstdir}/doc/EXAMPLE_05_POP
%doc %{geminstdir}/doc/EXAMPLE_06_HASHTABLE
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec


%changelog
* Mon Oct  3 2011 Jeff Goldschrafe <jeff@holyhandgrenade.org> - 0.6.7-1.hhg
- Rebuild for Ruby Enterprise Edition

* Fri Apr 29 2011 Sergio Rubio <rubiojr@frameos.org> - 0.6.7-1
- Initial package
