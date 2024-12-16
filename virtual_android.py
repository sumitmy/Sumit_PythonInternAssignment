import subprocess
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def create_virtual_android():
    try:
        command = "emulator -avd Medium_Phone_API_35"
        subprocess.Popen(command, shell=True)
        logging.info("Virtual Android system is launching...")
    except Exception as e:
        logging.error(f"Error occurred while starting the Android system: {e}")

def install_apk(apk_path):
    try:
        command = f"adb install {apk_path}"
        subprocess.run(command, shell=True, check=True)
        logging.info(f"APK installed successfully: {apk_path}")
    except Exception as e:
        logging.error(f"Error occurred while installing the APK: {e}")

def retrieve_system_info():
    try:
        os_version = subprocess.check_output("adb shell getprop ro.build.version.release", shell=True)
        memory_info = subprocess.check_output("adb shell cat /proc/meminfo", shell=True)

        logging.info(f"OS Version: {os_version.strip().decode()}")
        logging.info(f"Memory Info: {memory_info.decode()}")
    except Exception as e:
        logging.error(f"Error occurred while retrieving system information: {e}")

if __name__ == "__main__":
    apk_file = "calculator.apk"

    create_virtual_android()
    install_apk(apk_file)
    retrieve_system_info()
