{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 馃幃 Compilar CodeQuest APK\n",
    "\n",
    "Este notebook compila tu app **CodeQuest** en un APK instalable.\n",
    "\n",
    "鈴憋笍 **Tiempo estimado:** 15-20 minutos\n",
    "\n",
    "---"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Paso 1: Preparar entorno\n",
    "\n",
    "Ejecuta esta celda para instalar las herramientas necesarias."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Instalar Java y herramientas\n",
    "!apt-get update -y\n",
    "!apt-get install -y openjdk-17-jdk autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev automake wget\n",
    "\n",
    "# Configurar Java\n",
    "import os\n",
    "os.environ['JAVA_HOME'] = '/usr/lib/jvm/java-17-openjdk-amd64'\n",
    "\n",
    "# Instalar buildozer\n",
    "!pip install buildozer cython\n",
    "\n",
    "print(\"鉁� Entorno preparado correctamente\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Paso 2: Descargar tu c贸digo desde GitHub"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Crear carpeta del proyecto\n",
    "!mkdir -p codequest\n",
    "%cd codequest\n",
    "\n",
    "# Descargar main.py desde tu repositorio\n",
    "!curl -L -o main.py \"https://raw.githubusercontent.com/darkcity52-hash/hell-quest/main/main.py\"\n",
    "\n",
    "# Descargar icono\n",
    "!curl -L -o icon.png \"https://raw.githubusercontent.com/darkcity52-hash/hell-quest/main/icon.png\"\n",
    "\n",
    "# Verificar descarga\n",
    "!ls -la\n",
    "\n",
    "print(\"鉁� C贸digo descargado\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Paso 3: Crear archivo buildozer.spec\n",
    "\n",
    "Este archivo configura c贸mo se compila tu APK."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "%%writefile buildozer.spec\n",
    "[app]\n",
    "title = CodeQuest\n",
    "package.name = codequest\n",
    "package.domain = org.codequest\n",
    "source.dir = .\n",
    "source.include_exts = py,png,jpg,kv,atlas,json\n",
    "version = 1.0.0\n",
    "requirements = python3,kivy\n",
    "presplash.filename = presplash.png\n",
    "icon.filename = icon.png\n",
    "orientation = portrait\n",
    "fullscreen = 0\n",
    "android.permissions = VIBRATE,WRITE_EXTERNAL_STORAGE\n",
    "android.api = 33\n",
    "android.minapi = 21\n",
    "android.ndk = 25b\n",
    "android.sdk = 33\n",
    "android.accept_sdk_license = True\n",
    "\n",
    "[buildozer]\n",
    "log_level = 2\n",
    "warn_on_root = 1"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Paso 4: Descargar pantalla de carga"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Descargar presplash\n",
    "!curl -L -o presplash.png \"https://raw.githubusercontent.com/darkcity52-hash/hell-quest/main/presplash.png\"\n",
    "\n",
    "print(\"鉁� Imagen de carga descargada\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Paso 5: Compilar APK 鈴憋笍\n",
    "\n",
    "**鈿狅笍 IMPORTANTE:** Esta celda tarda **15-20 minutos**.\n",
    "\n",
    "No cierres el navegador mientras compila."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Compilar APK (esto tarda 15-20 minutos)\n",
    "!buildozer android debug\n",
    "\n",
    "print(\"鉁� Compilaci贸n completada\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Paso 6: Descargar el APK\n",
    "\n",
    "Una vez terminado, el APK estar谩 en la carpeta `bin/`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Mostrar ubicaci贸n del APK\n",
    "!ls -la bin/\n",
    "\n",
    "from google.colab import files\n",
    "import os\n",
    "\n",
    "# Buscar el APK\n",
    "apk_files = [f for f in os.listdir('bin') if f.endswith('.apk')]\n",
    "if apk_files:\n",
    "    apk_path = f'bin/{apk_files[0]}'\n",
    "    print(f\"\\n馃摝 APK encontrado: {apk_path}\")\n",
    "    print(f\"馃搹 Tama帽o: {os.path.getsize(apk_path) / (1024*1024):.2f} MB\")\n",
    "    print(\"\\n馃摜 Descargando APK...\")\n",
    "    files.download(apk_path)\n",
    "else:\n",
    "    print(\"鉂� No se encontr贸 el APK. Revisa los errores arriba.\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "---\n",
    "\n",
    "## 鉁� 隆Listo!\n",
    "\n",
    "El APK deber铆a haberse descargado a tu dispositivo.\n",
    "\n",
    "### Para instalar:\n",
    "1. Abre el archivo APK descargado\n",
    "2. Permite instalaci贸n de fuentes desconocidas si lo pide\n",
    "3. Instala y disfruta 馃幃"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "name": "python",
   "version": "3.10.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
