import io
import struct

class open_ext:
    def __init__ (self, *args):
        self.file = open(*args)

    def __getattr__(self, attr):
        return getattr(self.file, attr)

    def __enter__ (self):
        return self

    def __exit__ (self, exc_type, exc_value, traceback):
        self.file.close()

    def eof(self):
        if not self.file.read(1):
            return True
        self.file.seek(-1, io.SEEK_CUR)
        return False

    def skip(self, bytes):
        self.file.seek(bytes, io.SEEK_CUR)

    def read_until_zero(self):
        out = b''
        byte = self.file.read(1)
        while byte != b"\x00":
            out += byte
            byte = self.file.read(1)
        return out

    def read_until_end(self):
        return self.file.read()

    def read_i8(self):
        return struct.unpack('b', self.file.read(1))[0]

    def read_i16_le(self):
        return struct.unpack('<h', self.file.read(2))[0]

    def read_i32_le(self):
        return struct.unpack('<i', self.file.read(4))[0]

    def read_u8(self):
        return struct.unpack('B', self.file.read(1))[0]

    def read_u16_le(self):
        return struct.unpack('<H', self.file.read(2))[0]

    def read_u32_le(self):
        return struct.unpack('<I', self.file.read(4))[0]

    def write_i8(self, x):
        self.file.write(struct.pack('b', x))

    def write_i16_le(self, x):
        self.file.write(struct.pack('<h', x))

    def write_i32_le(self, x):
        self.file.write(struct.pack('<i', x))

    def write_u8(self, x):
        self.file.write(struct.pack('B', x))

    def write_u16_le(self, x):
        self.file.write(struct.pack('<H', x))

    def write_u32_le(self, x):
        self.file.write(struct.pack('<I', x))
