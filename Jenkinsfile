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

    stage('Import Images into K3s') {
      steps {
        sh '''
        docker save service-a | k3s ctr images import -
        docker save service-b | k3s ctr images import -
        docker save service-c | k3s ctr images import -
        '''
      }
    }

    stage('Deploy') {
      steps {
        sh 'kubectl apply -f k8s/'
      }
    }

    stage('Verify') {
      steps {
        sh 'kubectl get pods'
      }
    }
  }
}
