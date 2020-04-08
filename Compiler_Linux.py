import ctypes

DRIVE_REMOVABLE   = 2

DRIVE_TYPE_MAP = { DRIVE_REMOVABLE   : 'DRIVE_REMOVABLE'}

def get_drive_info():
    result = []
    bitmask = ctypes.windll.kernel32.GetLogicalDrives()
    for i in range(26):
        bit = 2 ** i
        if bit & bitmask:
            drive_letter = '%s:' % chr(65 + i)
            drive_type = ctypes.windll.kernel32.GetDriveTypeA('%s\\' % drive_letter)
            result.append((drive_letter, drive_type))
    return result

# Test
if __name__ == '__main__':
    drive_info = get_drive_info()
    for drive_letter, drive_type in drive_info:
        print('%s = %s' % (drive_letter, DRIVE_TYPE_MAP[drive_type]))
    removable_drives = [drive_letter for drive_letter, drive_type in drive_info if drive_type == DRIVE_REMOVABLE]
    print('removable_drives = %r' % removable_drives)