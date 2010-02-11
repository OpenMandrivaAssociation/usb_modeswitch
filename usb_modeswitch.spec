%define name    usb_modeswitch
%define fname	usb-modeswitch
%define version 1.1.0
%define	fver	%{version}
%define rel	2

Name:           %{name}
Summary:        Activating Switchable USB Devices on Linux
Version:        %{version}
Release:        %mkrel %{rel}
License:        GPLv2
Source:         http://www.draisberghof.de/usb_modeswitch/%{fname}-%{fver}.tar.bz2
URL:            http://www.draisberghof.de/usb_modeswitch/
Group:          System/Configuration/Hardware
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:	kernel-source
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
%setup -q -n %{fname}-%{fver}

%build
rm -f usb-modeswitch
gcc -O -Wall -o usb_modeswitch usb_modeswitch.c -l usb

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_sbindir} \
	%{buildroot}%{_sysconfdir} \
	%{buildroot}%{_sysconfdir}/udev/rules.d \
	%{buildroot}%{_sysconfdir}/usb_modeswitch.d \
	%{buildroot}%{_mandir}/man1 \
	%{buildroot}/lib/udev

install -m 755 usb_modeswitch %{buildroot}%{_sbindir}
install -m 644 usb_modeswitch.conf %{buildroot}%{_sysconfdir}/usb-modeswitch.conf
install -m 644 40-usb_modeswitch.rules %{buildroot}%{_sysconfdir}/udev/rules.d/91-usb_modeswitch.rules
install -m 644 ./usb_modeswitch.d/* %{buildroot}%{_sysconfdir}/usb_modeswitch.d/
install -m 755 ./usb_modeswitch.sh %{buildroot}//lib/udev/usb_modeswitch
install -m 644 ./usb_modeswitch.1 %{buildroot}%{_mandir}/man1/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%dir %{_sysconfdir}/usb_modeswitch.d
/lib/udev/usb_modeswitch
%{_sbindir}/*
%{_mandir}/man1/*
%attr(644,root,root) %config(noreplace) %{_sysconfdir}/usb_modeswitch.d/*
%attr(644,root,root) %config(noreplace) %{_sysconfdir}/usb-modeswitch.conf
%attr(644,root,root) %config(noreplace) %{_sysconfdir}/udev/rules.d/91-usb_modeswitch.rules
