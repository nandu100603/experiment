pipeline {
    agent any
    tools{
        ant '1.10.14'
    }

    stages {
        stage('Checkout') {
            steps {
                
                checkout scm
            }
        }

        stage('Python Changes') {
            when {
                changeset '**/Python/**'
            }
            steps {
                script {
                   
                    def pythonDir = 'Python/'
                    def changedFiles = getChangedFiles(pythonDir)
                    if (changedFiles) {
                        echo "Python code changes detected in the following files:"
                        echo changedFiles.join('\n')
                        for (def file : changedFiles) {
                            if (file.contains("/Test")) {
                                def result = bat(script: "python $file", returnStatus: true)
                                if (result == 0) {
                                echo "Success: Python script executed successfully."
                                mail bcc: '', body: '''Hi
                                Successfully executed the code and tested ''', cc: '', from: '', replyTo: '', subject: 'Jenkins Job', to: '20951a1248@iare.ac.in'

                            } else {
                                 mail bcc: '', body: '''Hi
                                failured occur executing the code ''', cc: '', from: '', replyTo: '', subject: 'Jenkins Job', to: '20951a1248@iare.ac.in'
                                echo "Failure: Python script execution failed with exit code $result."
                            }

                                echo "Content of $file:"
                                echo readFile(file)
                            }
                        /*
                            def response = httpRequest acceptType: 'APPLICATION_JSON', contentType: 'APPLICATION_OCTETSTREAM',
                           httpMode: 'POST', multipartName: 'file', quiet: true,
                           responseHandle: 'NONE', timeout: null, uploadFile: "$file",
                           url: 'http://localhost:8080/upload'

                            if (response.status == 200) {
                               
                                echo "HTTP request was successful"
                                echo "Response: ${response}"
                            } else {
                                
                                echo "HTTP request failed with status code: ${response.status}"
                                echo "Response: ${response}"
                            }
                            */

                        }


                    } 
                    else {
                        echo "Python code changes detected, but no specific files found."
                    }
                }
            }
        }

        stage('Java Changes') {
            when {
                changeset '**/Java/**'
            }
            steps {
                script {
                  
                    def javaDir = 'Java/'
                    def srcDir = "Java/src/com"
                    def testDir = "Java/test/com"
                    def buildDir = "Java/build"

                    //bat "rd /s /q $buildDir"

                    def changedFiles = getChangedFiles(srcDir)
                    def testFiles = getChangedFiles(testDir)

                    if (changedFiles) {
                        echo "Java code changes detected in the following files:"
                        echo changedFiles.join('\n')
                        for (def file : changedFiles) {
                            def className = file.replaceAll('.*/(.*).java', '$1')
                            def buildpath = 'Java/build.xml'
                            try {
                                
                                bat "ant -f $buildpath -Djava.file=$file -Dmain.class=$className compile"
                                bat "ant -f $buildpath -Djava.file=$className -Dmain.class=$className run"
                                echo "Java code in $file executed successfully."
                                mail bcc: '', body: "Successfully Executed $file", subject: 'Jenkins Job', to: '20951a1284@iare.ac.in'

                            } catch (Exception e) {
                               
                                currentBuild.result = 'FAILURE'
                                echo "Error in $file: $e.getMessage()"
                                mail bcc: '', body: "Error in $file: $e.getMessage()", subject: 'Jenkins Job', to: '20951a1284@iare.ac.in'
                            }
                        }
                    }
                    else {
                        echo "Java code changes detected, but no specific files found."
                    }
                    if (testFiles) {
                        echo "JUnit test changes detected in the following files:"
                        echo testFiles.join('\n')
                        for (def testFile : testFiles) {
                            def buildpath = "Java/build.xml"
                            try {
                                echo "$srcDir"
                                bat "ant -f $buildpath -Dbuild.dir=$buildDir -Dsrc.dir=src/com -Dtest.dir=test/com test"
                                echo "JUnit tests in $testFile executed successfully."
                                mail bcc: '', body: "Successfully Executed $testFile", subject: 'Jenkins Job', to: '20951a1284@iare.ac.in'

                            } catch (Exception e) {
                                echo "Error in $testFile: $e.getMessage()"
                                mail bcc: '', body: "Error in $testFile: $e.getMessage()", subject: 'Jenkins Job', to: '20951a1284@iare.ac.in'
                            }
                        }
                    } else {
                        echo "JUnit test changes detected, but no specific files found."
                    }                
                        /*
                            def response = httpRequest acceptType: 'APPLICATION_JSON', contentType: 'APPLICATION_OCTETSTREAM',
                           httpMode: 'POST', multipartName: 'file', quiet: true,
                           responseHandle: 'NONE', timeout: null, uploadFile: "$file",
                           url: 'http://localhost:8080/upload'

                            if (response.status == 200) {
                                
                                echo "HTTP request was successful"
                                echo "Response: ${response}"
                            } else {
                                
                                echo "HTTP request failed with status code: ${response.status}"
                                echo "Response: ${response}"
                            }
                        */

  
                        
                    } 
            }
                    
                
        }

        stage('CPP Changes') {
            when {
                changeset '**/CPP/**'
            }
            steps {
                script {
                   
                    def cppDir = 'CPP/'

                    
                    def changedFiles = getChangedFiles(cppDir)

                    if (changedFiles) {
                        echo "C++ code changes detected in the following files:"
                        echo changedFiles.join('\n')

                        for (def file : changedFiles) {
                            echo "Content of $file:"
                            echo readFile(file)
                        /*
                            def response = httpRequest acceptType: 'APPLICATION_JSON', contentType: 'APPLICATION_OCTETSTREAM',
                           httpMode: 'POST', multipartName: 'file', quiet: true,
                           responseHandle: 'NONE', timeout: null, uploadFile: "$file",
                           url: 'http://localhost:8080/upload'

                            if (response.status == 200) {
                               
                                echo "HTTP request was successful"
                                echo "Response: ${response}"
                            } else {
                              
                                echo "HTTP request failed with status code: ${response.status}"
                                echo "Response: ${response}"
                            }
                        */

                        }


                    } else {
                        echo "C++ code changes detected, but no specific files found."
                    }
                }
            }
        }

        
    }
}

@NonCPS
List<String> getChangedFiles(String directory) {
    def changedFiles = []
    for (changeLogSet in currentBuild.changeSets) {
        for (entry in changeLogSet.getItems()) {
          
            if (entry.affectedPaths.any { it.startsWith(directory) }) {
                changedFiles.addAll(entry.affectedPaths)
            }
        }
    }
    return changedFiles
}


//java -jar jenkins.war --httpPort=9191


