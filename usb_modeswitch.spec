%define name    usb_modeswitch
%define version 0.9.4
%define	fver	0.9.4beta2
%define rel	0.beta2.1

Name:           %{name}
Summary:        Activating Switchable USB Devices on Linux
Version:        %{version}
Release:        %mkrel %{rel}
License:        GPL
Source:         http://www.draisberghof.de/usb_modeswitch/usb_modeswitch-%{fver}.tar.bz2
URL:            http://www.draisberghof.de/usb_modeswitch/
Group:          System/Configuration/Hardware
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:	kernel-source
BuildRequires:	libusb-devel
Requires:	sysfsutils

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
%setup -q -n %{name}-%{fver}

%build
rm -f usb_modeswitch
gcc -O -o usb_modeswitch usb_modeswitch.c -l usb

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_sbindir} \
	%{buildroot}%{_sysconfdir} \
	%{buildroot}%{_sysconfdir}/udev/rules.d

install -m 755 usb_modeswitch %{buildroot}%{_sbindir}
install -m 644 usb_modeswitch.conf %{buildroot}%{_sysconfdir}

cat > %{buildroot}%{_sysconfdir}/udev/rules.d/91-usb_modeswitch.rules <<EOF
SUBSYSTEMS=="usb", ATTRS{idVendor}=="05c6", ATTRS{idProduct}=="1000", RUN+="%{_sbindir}/usb_modeswitch"
EOF

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_sbindir}/*
%attr(644,root,root) %config(noreplace) %{_sysconfdir}/usb_modeswitch.conf
%attr(644,root,root) %config(noreplace) %{_sysconfdir}/udev/rules.d/91-usb_modeswitch.rules

