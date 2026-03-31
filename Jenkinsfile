pipeline {
  agent any

  environment {
    KUBECONFIG = "/home/jenkins/.kube/config"
  }

  stages {

    stage('Build Docker Images') {
      steps {
        sh '''
        docker build -t service-a ./service-a
        docker build -t service-b ./service-b
        docker build -t service-c ./service-c
        '''
      }
    }

    stage('Deploy to Kubernetes') {
      steps {
        sh 'kubectl apply -f k8s/'
      }
    }

    stage('Verify') {
      steps {
        sh '''
        kubectl get pods
        kubectl get svc
        '''
      }
    }
  }
}
