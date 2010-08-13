%define	dataver	20100707

Name:		usb_modeswitch
Summary:	Activating Switchable USB Devices on Linux
Version:	1.1.3
Release:	%mkrel 1
License:	GPLv2+
%define fname	usb-modeswitch
%define	fver	%{version}
Source0:	http://www.draisberghof.de/usb_modeswitch/%{fname}-%{fver}.tar.bz2
Source1:	http://www.draisberghof.de/usb_modeswitch/usb-modeswitch-data-%{dataver}.tar.bz2
# (proyvind): added by myself, submitted upstream
Patch0:		usb-modeswitch-data-20100707-samsung-4g.patch
# http://www.draisberghof.de/usb_modeswitch/bb/viewtopic.php?t=437
Patch1:		usb-modeswitch-1.1.3-add-waitbefore-and-resetnew-options.patch
# (proyvind): just make sure that libusb will be linked against, and it's not a
# compiler flag, but a linker flag.. submitted upstream..
Patch2:		usb-modeswitch-1.1.3-mandatory-libusb-LINKING.patch
URL:		http://www.draisberghof.de/usb_modeswitch/
Group:		System/Configuration/Hardware
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:	libusb-devel
Requires:	sysfsutils
Requires:	tcl

%description
USB_ModeSwitch is a mode switching tool for controlling "flip flop"
(multiple device) USB gear.

Several new USB devices (especially high-speed wireless WAN stuff,
they're expensive anyway) have their Windows drivers onboard; when
plugged in for the first time they act like a flash storage and start
installing the driver from there. After that (and on every consecutive
plugging) this driver switches the mode internally, the storage device
vanishes (in most cases), and a new device (like an USB modem) shows
up. The WWAN gear maker Option calls that feature "ZeroCD (TM)".


%prep
%setup -q -n %{fname}-%{fver} -a1
%patch0 -p0
%patch1 -p1 -b .waitbefore~
%patch2 -p1 -b .libusb_LINK~

%build
export CFLAGS="%{optflags}" LDFLAGS="%{ldflags}"
%make

%install
rm -rf %{buildroot}
%makeinstall_std
%makeinstall_std -C usb-modeswitch-data-%{dataver}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%dir %{_sysconfdir}/usb_modeswitch.d
/lib/udev/usb_modeswitch
%{_sbindir}/*
%{_mandir}/man1/*
%attr(644,root,root) %{_sysconfdir}/usb_modeswitch.d/*
%attr(644,root,root) %config(noreplace) %{_sysconfdir}/usb_modeswitch.conf
%attr(644,root,root) /lib/udev/rules.d/40-usb_modeswitch.rules
