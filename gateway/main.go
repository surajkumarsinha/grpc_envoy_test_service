package main

import (
	"context"
	"fmt"
	"log"
	"net/http"

	gw "pygrpcdemo/pb"

	"github.com/grpc-ecosystem/grpc-gateway/v2/runtime"
	"google.golang.org/grpc"
)

const (
	grpcServerEndpoint = "localhost:%s"
)

func main() {
	ctx := context.Background()
	ctx, cancel := context.WithCancel(ctx)
	defer cancel()

	mux := runtime.NewServeMux()
	opts := []grpc.DialOption{grpc.WithInsecure()}
	err := gw.RegisterDataServiceHandlerFromEndpoint(ctx, mux, fmt.Sprintf(grpcServerEndpoint, "8080"), opts)
	if err != nil {
		log.Fatalf("Failed to register gRPC gateway service endpoint: %v", err)
	}
	log.Println("Listening on port 8081")
	if err := http.ListenAndServe(":8081", mux); err != nil {
		log.Fatalf("Could not setup HTTP endpoint: %v", err)
	}
}