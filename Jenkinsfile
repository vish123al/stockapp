def gitCommit() {
    sh "git rev-parse HEAD > GIT_COMMIT"
    def gitCommit = readFile('GIT_COMMIT').trim()
    sh "rm -f GIT_COMMIT"
    return gitCommit
}

node {

    // Checkout source code from Git
    stage 'Checking out scm for repository'
    checkout scm
    stage '(TEST) unit/integration testing'
    //sh 'make test'
    stage '(BUILD) building image'
    sh "docker build -t vishaldenge/stocknew:${gitCommit()} ."
    sh "docker login -u vishaldenge -p 'v!sh@l123' "
    stage '(PUBLISH) Pushing the image '
    sh "docker push vishaldenge/stocknew:${gitCommit()}"
     stage '(DEPLOY) Deploying the container'
    //sh 'curl -X POST -H "Content-Type: application/json" http://10.0.1.85:8080/v2/groups -d@marathon2.json'
    marathon(
        url: 'http://10.0.1.85:8080',
        forceUpdate: true,
        filename: 'marathon.json',
        appId: 'blog',
        docker: "vishaldenge/stocknew:${gitCommit()}".toString()
    )
   
        stage 'Collect test reports'
        
         sh 'touch reports/*.xml'
         junit '**/reports/*.xml'
       // step([$class: 'JUnitResultArchiver', testResults: '**/reports/*.xml'])
        stage 'Clean up'
       
                         
   

}
