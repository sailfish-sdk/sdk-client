# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.25
# 

Name:       sdk-client

# >> macros
# << macros

Summary:    Mer SDK client tools
Version:    0.1
Release:    1
Group:      Development Platform/Platform SDK
License:    GPLv2+
Source0:    sdk-client.tar.bz2
Source100:  sdk-client.yaml

%description
Tools to support the Mer Qt Creator


%prep
%setup -q -n src

# >> setup
# << setup

%build
# >> build pre
# << build pre


make %{?jobs:-j%jobs}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
# << install post


%files
%defattr(-,root,root,-)
%{_bindir}/install-rpm
# >> files
# << files
