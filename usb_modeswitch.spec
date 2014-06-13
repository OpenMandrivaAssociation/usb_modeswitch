Name:		usb_modeswitch
Summary:	Activating Switchable USB Devices on Linux
Version:	2.2.0
Release:	2
License:	GPLv2+
%define fname	usb-modeswitch
%define	fver	%{version}
Source0:	http://www.draisberghof.de/usb_modeswitch/%{fname}-%{version}.tar.bz2
# (proyvind): fix a warning revealed with optimizations enabled and enable them
#             by default so that they'll get catched by upstream in the future.
#             Submitted upstream
#Patch0:		usb-modeswitch-1.1.9-catch-and-fix-more-warnings.patch
URL:		http://www.draisberghof.de/usb_modeswitch/
Group:		System/Configuration/Hardware
Source1:	usb_modeswitch.rpmlintrc
BuildRequires:	usb-compat-devel
Requires:	sysfsutils
Requires(pre):	tcl
Requires:	usb_modeswitch-data >= 20110805

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
%setup -q -n %{fname}-%{version}
#patch0 -p1 -b .warnings~

%build
%make CC=%{__cc} CFLAGS="%{optflags}" LDFLAGS="%{ldflags}"

%install
%makeinstall_std

%files
/lib/udev/usb_modeswitch
%{_sbindir}/*
%{_mandir}/man1/*
%config(noreplace) %{_sysconfdir}/usb_modeswitch.conf
