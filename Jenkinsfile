pipeline {
    agent any
    
    environment {
        RPM_PACKAGE_NAME = 'calc_files'
        DEB_PACKAGE_NAME = 'calc-files'
        PACKAGE_VERSION = '1.0'
    }
    
    stages {
        stage('Test Script') {
            steps {
                sh 'chmod +x calc_files.sh'
                sh 'bash -n calc_files.sh'
                sh './calc_files.sh || true'
            }
        }

        stage('Build RPM') {
            agent {
                docker {
                    image 'fedora:41'
                    args '-u root'
                }
            }
            steps {
                sh '''
                dnf install -y rpm-build rpmdevtools tar
                rpmdev-setuptree

                mkdir -p ~/rpmbuild/SOURCES/${RPM_PACKAGE_NAME}-${PACKAGE_VERSION}
                cp calc_files.sh ~/rpmbuild/SOURCES/${RPM_PACKAGE_NAME}-${PACKAGE_VERSION}/
                
                cd ~/rpmbuild/SOURCES
                tar czvf ${RPM_PACKAGE_NAME}-${PACKAGE_VERSION}.tar.gz ${RPM_PACKAGE_NAME}-${PACKAGE_VERSION}

                cp ${WORKSPACE}/rpm/calc_files.spec ~/rpmbuild/SPECS/
                rpmbuild -ba ~/rpmbuild/SPECS/calc_files.spec

                cp ~/rpmbuild/RPMS/noarch/*.rpm ${WORKSPACE}/
                '''
            }
        }

        stage('Build DEB') {
            agent {
                docker {
                    image 'ubuntu:22.04'
                    args '-u root'
                }
            }
            steps {
                sh '''
                apt-get update
                apt-get install -y build-essential debhelper devscripts

                mkdir -p build/${DEB_PACKAGE_NAME}-${PACKAGE_VERSION}
                cp calc_files.sh build/${DEB_PACKAGE_NAME}-${PACKAGE_VERSION}/
                cp -r debian build/${DEB_PACKAGE_NAME}-${PACKAGE_VERSION}/

                cd build/${DEB_PACKAGE_NAME}-${PACKAGE_VERSION}
                chmod +x debian/rules
                dpkg-buildpackage -us -uc -b

                cp ../*.deb ${WORKSPACE}/
                '''
            }
        }

        stage('Test RPM Installation') {
            agent {
                docker {
                    image 'fedora:41'
                    args '-u root'
                }
            }
            steps {
                sh '''
                rpm -ivh ${RPM_PACKAGE_NAME}-*.rpm
                which calc_files
                rpm -e ${RPM_PACKAGE_NAME}
                '''
            }
        }

        stage('Test DEB Installation') {
            agent {
                docker {
                    image 'ubuntu:22.04'
                    args '-u root'
                }
            }
            steps {
                sh '''
                dpkg -i ${DEB_PACKAGE_NAME}_*.deb || apt-get install -f -y
                
                which calc_files.sh
                
                apt-get remove -y ${DEB_PACKAGE_NAME}
                '''
            }
        }
    }

    post {
        success {
            archiveArtifacts artifacts: '*.rpm, *.deb'
            echo 'Build completed successfully'
        }
        failure {
            echo 'Build failed'
        }
        always {
            cleanWs()
        }
    }
}
