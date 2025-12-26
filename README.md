# System Programming & DevOps Project

This repository contains practical implementations of system programming tasks, package management, and DevOps automation pipelines.

## 📂 Project Structure

* **Scripting**:
    * `calc_files.sh` — A Bash script that calculates the number of regular files in the `/etc` directory.

* **Packaging**:
    * **RPM**: `rpm/calc_files.spec` — Specification file for building RPM packages (Fedora/RHEL).
    * **DEB**: `debian/` — Configuration files for building DEB packages (Ubuntu/Debian).

* **CI/CD & Automation**:
    * `Jenkinsfile` — A declarative pipeline that automates testing, building, and verifying installation of both RPM and DEB packages using Docker agents.
    * `.github/workflows/build.yml` — GitHub Actions workflow for CI.

* **Infrastructure**:
    * `docker/` — Docker Compose setup to run a Jenkins Master and a specialized Build Agent.

## 🚀 Usage

### 1. Run the Script
```bash
chmod +x calc_files.sh
sudo ./calc_files.sh
```

### 2. Build Jenkins Environment
To deploy the local CI/CD infrastructure:
```bash
cd docker
docker-compose up -d --build
```

## 👤 Author
Kiril Vasylenko
