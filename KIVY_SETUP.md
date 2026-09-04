# GUIA DE COMPILACAO KIVY - APK

## 🚀 Pré-requisitos

- Python 3.9+
- Git
- Java JDK 11+
- Android SDK
- Buildozer

## 📥 Instalação do Buildozer

### Windows:
```bash
pip install buildozer
pip install cython
pip install kivy
```

### Linux/Mac:
```bash
sudo apt-get install build-essential libssl-dev libffi-dev python3-dev
pip install buildozer cython kivy
```

## 🔧 Setup Android

### 1. Download Android SDK
```bash
# Windows - use Android Studio ou:
# Download em: https://developer.android.com/studio
```

### 2. Variáveis de Ambiente (importante!)

**Windows:**
```
ANDROID_SDK_ROOT=C:\Android\sdk
ANDROID_HOME=C:\Android\sdk
```

**Linux/Mac:**
```bash
export ANDROID_SDK_ROOT=$HOME/Android/Sdk
export ANDROID_HOME=$HOME/Android/Sdk
export PATH=$PATH:$ANDROID_SDK_ROOT/tools
```

## 📦 Compilar APK

### 1. Clone o repositório
```bash
git clone https://github.com/moisesrodriges530-hue/Proxy-Gking-v1.git
cd Proxy-Gking-v1
```

### 2. Instale dependências
```bash
pip install -r requirements.txt
pip install kivy buildozer cython
```

### 3. Compile para APK (DEBUG)
```bash
buildozer android debug
```

### 4. Compile para APK (RELEASE - Profissional)
```bash
buildozer android release
```

## ⏱️ Tempo de Compilação
- **Primeira vez:** 15-30 min (download NDK)
- **Próximas:** 5-10 min

## 📍 Localização do APK

Após compilar, o APK estará em:
```
bin/proxygking-1.0-debug.apk (DEBUG)
bin/proxygking-1.0-release.apk (RELEASE)
```

## 📱 Instalar no Celular

### Via USB:
```bash
adb install bin/proxygking-1.0-debug.apk
```

### Via arquivo:
1. Copie o APK para o celular
2. Instale normalmente

## 🐛 Troubleshooting

### "buildozer not found"
```bash
pip install --upgrade buildozer
```

### "ANDROID_SDK_ROOT not set"
Configure as variáveis de ambiente (veja acima)

### "Erro de compilação"
```bash
buildozer android debug -- log_level=2
```

### "NDK não encontrado"
Buildozer baixa automaticamente, aguarde a primeira compilação

## ✅ Pronto!
Seu APK está compilado e pronto para instalar! 🎉