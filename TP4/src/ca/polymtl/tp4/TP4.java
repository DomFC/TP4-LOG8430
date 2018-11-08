package ca.polymtl.tp4;

import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.PathParam;
import javax.ws.rs.Produces;
import javax.ws.rs.QueryParam;

@Path("/rest")
public class TP4 {
	@GET
	@Path("/hello/{name}")
	@Produces("text/plain")
	public String Hello(@PathParam("name") String name) {
		String val = "Hello " + name;
		System.out.println(val);
		return val;
	}
	
	@GET
	@Path("/numWords")
	@Produces("text/plain")
	public String NumWords(@QueryParam("text") String text) {
		String val = "Words: " + text.split(" ").length;
		System.out.println(val);
		return val;
	}
}
