pipeline {
  agent any

  environment {
    KUBECONFIG = "/home/jenkins/.kube/config"
  }

  stages {

    stage('Clone Repo') {
      steps {
        git 'https://github.com/Rishitha2707/3-tier-architecture.git'
      }
    }

    stage('Build Docker Images') {
      steps {
        sh '''
        docker build -t service-a:latest ./service-a
        docker build -t service-b:latest ./service-b
        docker build -t service-c:latest ./service-c
        '''
      }
    }

    stage('Import Images into K3s') {
      steps {
        sh '''
        docker save service-a:latest | k3s ctr images import -
        docker save service-b:latest | k3s ctr images import -
        docker save service-c:latest | k3s ctr images import -
        '''
      }
    }

    stage('Deploy to Kubernetes') {
      steps {
        sh '''
        kubectl apply -f k8s/
        '''
      }
    }

    stage('Verify Deployment') {
      steps {
        sh '''
        kubectl get pods
        kubectl get svc
        '''
      }
    }

  }

  post {
    success {
      echo '✅ Deployment Successful!'
    }
    failure {
      echo '❌ Deployment Failed!'
    }
  }
}
