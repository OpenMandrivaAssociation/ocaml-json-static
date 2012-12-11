Name:           ocaml-json-static
Version:        0.9.8
Release:        2
Summary:        OCaml JSON validator and converter (syntax extension)
License:        BSD
Group:          Development/Other
URL:            http://martin.jambon.free.fr/json-static.html
Source0:        http://martin.jambon.free.fr/json-static-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml >= 3.10.0
BuildRequires:  ocaml-findlib-devel
BuildRequires:  camlp4

# Make this dependency explicit because users won't be able
# to do much useful without it, and the automatic dependency
# checking script cannot pick it up.
Requires:       ocaml-json-wheel

%description
json-static is a tool for converting parsed JSON data with an
unchecked structure into specialized OCaml types and vice-versa.
It is a complement to the json-wheel library which provides a
parser and a (pretty-) printer.

%prep
%setup -q -n json-static-%{version}

%build
make

%install
rm -rf %{buildroot}
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs
make install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE README Changes yahoo.ml
%{_libdir}/ocaml/json-static



%changelog
* Wed May 09 2012 Crispin Boylan <crisb@mandriva.org> 0.9.8-2
+ Revision: 797705
- Rebuild

* Fri Sep 04 2009 Florent Monnier <blue_prawn@mandriva.org> 0.9.8-1mdv2011.0
+ Revision: 430879
- new version

* Tue Aug 25 2009 Florent Monnier <blue_prawn@mandriva.org> 0.9.7-1mdv2010.0
+ Revision: 420694
- update to new version 0.9.7

* Sun Jun 28 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.9.6-3mdv2010.0
+ Revision: 390243
- rebuild

* Sat Jun 27 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.9.6-2mdv2010.0
+ Revision: 390086
- rebuild

* Tue Jan 27 2009 Florent Monnier <blue_prawn@mandriva.org> 0.9.6-1mdv2009.1
+ Revision: 334593
- corrected group
- import ocaml-json-static

