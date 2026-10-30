import asyncio
import socket

PORT = 37541
MAGIC_STRING = 'BREED:ABORT'


def send_magic_packet():
    conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Allow broadcast
    conn.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    conn.sendto(MAGIC_STRING.encode(), ('255.255.255.255', PORT))
    conn.close()

async def send_abort_boot_packet():
    while True:
        send_magic_packet()
        print("Magic packet sent, waiting for reply...")
        await asyncio.sleep(0.5)

if __name__ == "__main__":
    try:
        # fir asyncio warning
        asyncio.run(send_abort_boot_packet())
    except KeyboardInterrupt:
        print("\nStopped by user.")
