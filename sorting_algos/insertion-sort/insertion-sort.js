function insertionSort(arr){
    for(let i = 0; i < arr.length; i++){
        let elem = arr[i];
        let sortedIndex = i - 1; // i or i-1 ?

        while(sortedIndex >= 0 && arr[sortedIndex] > elem){
            arr[sortedIndex + 1] = arr[sortedIndex];
            sortedIndex--;
        }     
        arr[sortedIndex + 1] = elem;
    }
 return arr;
}

function insertionSort(arr){
    for(let i = 0; i < arr.length; i++){
        let elem = arr[i];
        let sortedIndex = i - 1; 

        function helperRecur(index, num){

            // base case
            if(index < 0 || num >= arr[index]){
                arr[index + 1] = elem;
                return;
            }
            arr[index + 1] = arr[index];
            helperRecur(index - 1, num)
        }
        helperRecur(sortedIndex, elem)
        
    }
 return arr;
}