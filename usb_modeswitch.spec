Name:		usb_modeswitch
Summary:	Activating Switchable USB Devices on Linux
Version:	2.6.0
Release:	2
License:	GPLv2+
%define fname	usb-modeswitch
%define	fver	%{version}
Source0:	https://www.draisberghof.de/usb_modeswitch/%{fname}-%{version}.tar.bz2
URL:		https://www.draisberghof.de/usb_modeswitch/
Group:		System/Configuration/Hardware
Source1:	usb_modeswitch.rpmlintrc
BuildRequires:	pkgconfig(libusb-1.0)
BuildRequires:	systemd
BuildRequires:	systemd-rpm-macros
# To avoid a file dependency
BuildRequires:	tcl
Requires:	systemd
Requires:	usb_modeswitch-data >= 20170205

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
%autosetup -n %{fname}-%{version}

%build
%setup_compile_flags
%make_build CC=%{__cc} CFLAGS="%{optflags}" LDFLAGS="%{ldflags}" SBINDIR="%{_sbindir}"

%install
mkdir -p %{buildroot}%{_unitdir}
%make_install SYSDIR="%{buildroot}%{_unitdir}" UDEVDIR="%{buildroot}%{_prefix}/lib/udev" SBINDIR="%{buildroot}%{_sbindir}"

%files
%config(noreplace) %{_sysconfdir}/usb_modeswitch.conf
%{_prefix}/lib/udev/usb_modeswitch
%{_sbindir}/*
%{_unitdir}/*.service
%{_mandir}/man1/*
