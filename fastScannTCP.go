package main

//imports
import "fmt"
import "flag"
import "context"
import "strings"
import "strconv"
import "log"
import "sync"
import "time"
import "net"


// variable declarations
var server= flag.String("server","10.10.10.102", "Host or IP direction to scann ")
var ports= flag.String("range","1-65535","Ports range to scann : 80, 1-1024,2000-3000...")
var threads= flag.Int("thread",1000,"NUmber of threads to execute")
var timeout = flag.Duration("timeout",1*time.Second, "Seconds by port")

//Functions of input ports
func processRange(ctx context.Context, r string )chan int{
	c := make(chan int)
	done := ctx.Done()
	go func(){
		defer close(c)
		blocks := strings.Split(r,",")
		log.Println(blocks)
		for _, block := range blocks {
			rg := strings.Split(block,"-")
			var minPort, maxPort int
			var err error
			minPort, err = strconv.Atoi(rg[0])
			if err != nil{
				log.Print("exception on ranges minPort : ",block)
				continue
			}
			if len(rg)==1{
				maxPort =minPort
			}else{
				maxPort, err = strconv.Atoi(rg[1])
				if err != nil{
					log.Print("exception on ranges maxPort : ",block)
					continue
				}
			}
			for port := minPort; port <=maxPort ; port ++{
				select {
					case c <- port:
					case <- done:
						return
				}
			}
		}
	}()
	return c
}

//using threads for scann ports
func scanPorts(ctx context.Context, in <-chan int)chan string{
	out:= make(chan string)
	done := ctx.Done()
	var wg sync.WaitGroup
	wg.Add(*threads)

	for i := 0; i < *threads; i++ {
		go func(){
			defer wg.Done()
			for {
				select{
					case port , ok := <-in:
						if !ok {
							return
						}
						s := scanPort(port)
						select{
							case out <- s:
							case <-done :
								return
						}
					case  <- done:
						return
				}
			}
		}()
		go func(){
			wg.Wait()
			close(out)
		}()
	}
	return out

}
//scann basic port 
func scanPort(port int )string{
	addr:= fmt.Sprintf("%s:%d", *server, port)
	conn,err :=net.DialTimeout("tcp",addr,*timeout)
	if err != nil{
		return fmt.Sprintf("%d:  %s", port, err.Error())
	}
	conn.Close()
	return fmt.Sprintf("[+] %d: OPEN",port)
}


//______Main process______
func main() {
	ctx, cancel := context.WithCancel(context.Background())
	defer cancel()

	flag.Parse()
	fmt.Printf("\n[+] scann host %s (Ports: %s )\n\n", *server, *ports)
	pR := processRange(ctx, *ports);
	sP := scanPorts(ctx,pR)

	for port := range sP {
		if strings.HasSuffix(port,": OPEN"){
			fmt.Println(port)
		}
	}
}
