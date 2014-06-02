# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.22
# 
# >> macros
# << macros

Name:       kf5-kdesignerplugin
Summary:    KDE Frameworks 5 Tier 3 integration module for QtDesigner
Version:    4.99.0
Release:    1
Group:      System/Base
License:    GPLv2+
URL:        http://www.kde.org
Source0:    %{name}-%{version}.tar.xz
Source100:  kf5-kdesignerplugin.yaml
Source101:  kf5-kdesignerplugin-rpmlintrc
Requires:   kf5-filesystem
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Declarative)
BuildRequires:  pkgconfig(Qt5WebKit)
BuildRequires:  pkgconfig(Qt5WebKitWidgets)
BuildRequires:  pkgconfig(Qt5Designer)
BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-tools
BuildRequires:  kf5-kcoreaddons-devel
BuildRequires:  kf5-kconfig-devel
BuildRequires:  kf5-kdoctools-devel
BuildRequires:  kf5-kcompletion-devel
BuildRequires:  kf5-kconfigwidgets-devel
BuildRequires:  kf5-kiconthemes-devel
BuildRequires:  kf5-kio-devel
BuildRequires:  kf5-kitemviews-devel
BuildRequires:  kf5-kplotting-devel
BuildRequires:  kf5-ktextwidgets-devel
BuildRequires:  kf5-kwidgetsaddons-devel
BuildRequires:  kf5-kxmlgui-devel
BuildRequires:  kf5-sonnet-devel
BuildRequires:  kf5-kdewebkit-devel
BuildRequires:  qt5-qttools-qtdesigner


%description
KDE Frameworks 5 Tier 3 integration module for QtDesigner



%package devel
Summary:    Development files for %{name}
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   kf5-kcoreaddons-devel
Requires:   kf5-kconfig-devel
Requires:   kf5-kdoctools-devel
Requires:   kf5-kcompletion-devel
Requires:   kf5-kconfigwidgets-devel
Requires:   kf5-kiconthemes-devel
Requires:   kf5-kio-devel
Requires:   kf5-kitemviews-devel
Requires:   kf5-kplotting-devel
Requires:   kf5-ktextwidgets-devel
Requires:   kf5-kwidgetsaddons-devel
Requires:   kf5-kxmlgui-devel
Requires:   kf5-sonnet-devel
Requires:   kf5-kdewebkit-devel

%description devel
The %{name}-devel package contains the files necessary to develop applications
that use %{name}.



%prep
%setup -q -n %{name}-%{version}/upstream

# >> setup
# << setup

%build
# >> build pre
%kf5_make
# << build pre



# >> build post
# << build post
%install
rm -rf %{buildroot}
# >> install pre
%kf5_make_install
# << install pre

# >> install post
# << install post









%files
%defattr(-,root,root,-)
%doc COPYING.LIB README.md
%{_kf5_bindir}/kgendesignerplugin
%{_kf5_mandir}/man1/*
%{_kf5_qtplugindir}/designer/*.so
%{_kf5_datadir}/kf5/widgets/*
# >> files
# << files


%files devel
%defattr(-,root,root,-)
%{_kf5_libdir}/cmake/KF5DesignerPlugin
# >> files devel
# << files devel

